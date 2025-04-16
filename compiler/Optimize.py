import os
import sys
sys.path.append('./')
import itertools
from collections import defaultdict
from antlr4 import *
from simpleir.SimpleIRLexer import SimpleIRLexer
from simpleir.SimpleIRParser import SimpleIRParser
from simpleir.SimpleIRListener import SimpleIRListener
import logging
logging.basicConfig(level=logging.DEBUG)
import networkx as nx

class IRList(SimpleIRListener):

  def __init__(self):
    self.instr = []

  # Enter a parse tree produced by SimpleIRParser#unit.
  def enterUnit(self, ctx:SimpleIRParser.UnitContext):
    pass

  # Enter a parse tree produced by SimpleIRParser#function.
  def enterFunction(self, ctx:SimpleIRParser.FunctionContext):
    pass

  # Enter a parse tree produced by SimpleIRParser#localVariables.
  def enterLocalVariables(self, ctx:SimpleIRParser.LocalVariablesContext):
    pass

  # Enter a parse tree produced by SimpleIRParser#parameters.
  def enterParameters(self, ctx:SimpleIRParser.ParametersContext):
    pass

  # Enter a parse tree produced by SimpleIRParser#statements.
  def enterStatements(self, ctx:SimpleIRParser.StatementsContext):
    pass

  # Enter a parse tree produced by SimpleIRParser#returnStatement.
  def enterReturnStatement(self, ctx:SimpleIRParser.ReturnStatementContext):
    pass

  # Enter a parse tree produced by SimpleIRParser#end.
  def enterEnd(self, ctx:SimpleIRParser.EndContext):
    pass

  # Enter a parse tree produced by SimpleIRParser#statement.
  def enterStatement(self, ctx:SimpleIRParser.StatementContext):
    pass

  # Enter a parse tree produced by SimpleIRParser#operation.
  def enterOperation(self, ctx:SimpleIRParser.OperationContext):
    self.instr.append(ctx)

  # Enter a parse tree produced by SimpleIRParser#assign.
  def enterAssign(self, ctx:SimpleIRParser.AssignContext):
    self.instr.append(ctx)

  # Enter a parse tree produced by SimpleIRParser#dereference.
  def enterDereference(self, ctx:SimpleIRParser.DereferenceContext):
    self.instr.append(ctx)

  # Enter a parse tree produced by SimpleIRParser#reference.
  def enterReference(self, ctx:SimpleIRParser.ReferenceContext):
    self.instr.append(ctx)

  # Enter a parse tree produced by SimpleIRParser#assignDereference.
  def enterAssignDereference(self, ctx:SimpleIRParser.AssignDereferenceContext):
    self.instr.append(ctx)

  # Enter a parse tree produced by SimpleIRParser#call.
  def enterCall(self, ctx:SimpleIRParser.CallContext):
    self.instr.append(ctx)

  # Enter a parse tree produced by SimpleIRParser#label.
  def enterLabel(self, ctx:SimpleIRParser.LabelContext):
    self.instr.append(ctx)

  # Enter a parse tree produced by SimpleIRParser#gotoStatement.
  def enterGotoStatement(self, ctx:SimpleIRParser.GotoStatementContext):
    self.instr.append(ctx)

  # Enter a parse tree produced by SimpleIRParser#ifGoto.
  def enterIfGoto(self, ctx:SimpleIRParser.IfGotoContext):
    self.instr.append(ctx)

def visualize_graph(cfg, filename="graph.png"):
  # visualize graph
  A = nx.nx_agraph.to_agraph(cfg)
  # A.layout()
  A.draw(filename, prog="dot")

def textualize_graph(cfg):
  text = "Control Flow Graph\n"
  for node in sorted(cfg.nodes):
    text += f'BB{node}'
    text += str(", ".join([ f'->BB{x}{cfg[node][x]}' for x in cfg[node].keys() ]))
    text += "\n"
    text += "\n".join([ str(instr) for instr in cfg.nodes[node]["instrs"] ])
    text += "\n" if len(cfg.nodes[node]["instrs"]) > 0 else ""
    text += "\n"
  return text

def controlflow(instrs):
  """Takes a list of while3addr instructions and produces a control-flow graph as a networkx digraph"""
  assert len(instrs) > 0 # assume program has at least one instruction
  leaders = set()
  leaders.add(0) # 0 is always the beginning of the program and the first leader
  exitblock = len(instrs)
  leaders.add(exitblock) # add a leader for the exit block

  L = {}
  for i in range(len(instrs)):
    match type(instrs[i]):
      case SimpleIRParser.IfGotoContext | SimpleIRParser.GotoStatementContext:
        leaders.add(instrs[i].labelName.text)
        leaders.add(i + 1)
      case SimpleIRParser.LabelContext:
        L[instrs[i].labelName.text] = i + 1
        if instrs[i].labelName.text in leaders:
          leaders.remove(instrs[i].labelName.text)
          leaders.add(i)
      case _:
        continue
  sortedleaders = sorted(leaders)
  

  bbranges = [ (sortedleaders[x], sortedleaders[x + 1]) for x in range(0, len(sortedleaders) - 1) ]

  # # collect basic blocks, mapping their leaders to their lists of instructions
  bbinstrs = {} # map leader to instructions
  bbnums = {}
  bbnum = 1

  while bbnum < len(bbranges) + 1:
    s = slice(*bbranges[bbnum - 1])
    bbinstrs[sortedleaders[bbnum - 1]] = [i for i in instrs[s]]
    bbnums[sortedleaders[bbnum - 1]] = bbnum
    bbnum = bbnum + 1

  # # add exit block
  bbinstrs[exitblock] = []
  bbnums[exitblock] = bbnum

  # # collect edges and remove gotos since edges replace pc
  edges = []
  for n in bbinstrs:
    if n == exitblock:
      break
    i = bbinstrs[n][-1]
    match type(i):
      case SimpleIRParser.GotoStatementContext:
        t = L[i.labelName.text] - 1
        edges.append((bbnums[n], bbnums[t]))
      case SimpleIRParser.IfGotoContext:
        t = L[i.labelName.text] - 1
        edges.append((bbnums[n], bbnums[t], {'condition': True}))
        edges.append((bbnums[n], bbnums[n] + 1, {'condition': False}))
      case _:
        edges.append((bbnums[n], bbnums[n] + 1))
  nodes = [ (bbnums[leader], {'instrs': [i for i in bbinstrs[leader]]}) for leader in bbinstrs.keys() ]

  # # add entry block
  nodes.append((0, {'instrs': []}))
  edges.append((0, 1))
  # logging.debug(f'{nodes}')
  # logging.debug(f'{edges}')

  cfg = nx.DiGraph()
  cfg.add_nodes_from(nodes)
  cfg.add_edges_from(edges)

  return cfg

def reversecfg(cfg):
  """Reverse the graph edges and block instructions for backwards analysis."""
  # cfg = cfg.reverse() # Function not working due to networkx issues with modern Python?
  l = len(cfg.nodes)
  rnodes = [ (l - k - 1, {'instrs': cfg.nodes[k]['instrs']}) for k in cfg.nodes.keys()]
  redges = [ (l - o - 1, l - i - 1) for (i, o) in cfg.edges]
  rcfg = nx.DiGraph()
  rcfg.add_nodes_from(rnodes)
  rcfg.add_edges_from(redges)
  for node in rcfg.nodes:
    rcfg.nodes[node]['instrs'] = list(reversed(rcfg.nodes[node]['instrs']))
  
  return rcfg

def dataflow(cfg):
  """Perform a data-flow analysis on a cfg."""

  # # initialize state
  # for node in cfg.nodes:
  #    cfg.nodes[node]['instate'] = set()
  #    cfg.nodes[node]['outstate'] = set()
  #    cfg.nodes[node]['analysis'] = None

  # cfg.nodes[0]['instate'] = initial_state

  # worklist = deque(cfg.nodes)
  # while len(worklist) > 0:
  #   node = worklist.popleft()
  #   # logging.debug(f'iteration: {node}')
  #   cfg.nodes[node]['analysis'], cfg.nodes[node]['outstate'] = analyzeblock(cfg.nodes[node]['instate'], cfg.nodes[node]['instrs'], transfer)
  #   for succ in cfg.successors(node):
  #     newinput = join(cfg.nodes[succ]['instate'], cfg.nodes[node]['outstate'])
  #     if newinput != cfg.nodes[succ]['instate']:
  #       cfg.nodes[succ]['instate'] = newinput
  #       worklist.append(succ)

  return cfg

def getInstructions(cfg):
  print('function main')
  for n in cfg.nodes:
    for i in cfg.nodes[n]['instrs']:
      print(getFullText(i))
  print('return outparam')
  print('end function')

def getFullText(ctx):
  input_stream = ctx.start.getInputStream()
  text = input_stream.getText(ctx.start.start, ctx.stop.stop)
  return text

def recursiveLiveVars(cfg, entry_node, allvars, livevars):
  node = cfg.nodes[entry_node]
  newlive = set()
  newlive.update(livevars)
  for i in node['instrs']:
    match type(i):
      case SimpleIRParser.AssignContext:
        if i.variable.text not in newlive:
          continue
        newlive.remove(i.variable.text)
        if not i.operand.text.isdigit():
          newlive.add(i.operand.text)
          allvars.add(i.operand.text)
      case SimpleIRParser.OperationContext:
        if i.variable.text not in newlive:
          continue
        newlive.remove(i.variable.text)
        if not i.operand1.text.isdigit():
          newlive.add(i.operand1.text)
          allvars.add(i.operand1.text)
        if not i.operand2.text.isdigit():
          newlive.add(i.operand2.text)
          allvars.add(i.operand2.text)
      case _:
        continue

  if len(list(cfg.successors(entry_node))) == 0:
    return newlive, allvars

  oldlive = set()
  oldlive.update(newlive)
  newlive = set()
  for succ in cfg.successors(entry_node):
    l, a = recursiveLiveVars(cfg, succ, allvars, oldlive)
    newlive.update(l)
    allvars.update(a)
  return newlive, allvars

def deadCodeElimination(cfg, retvar='outparam'):
  rcfg = reversecfg(cfg)
  livevars = set()
  allvars = set()
  livevars, allvars = set(), set()
  livevars.add(retvar)
  allvars.add(retvar)
  live, usedvars = recursiveLiveVars(rcfg, 0, allvars, livevars)

  for node in cfg.nodes:
    for i in cfg.nodes[node]['instrs']:
      match type(i):
        case SimpleIRParser.AssignContext | SimpleIRParser.OperationContext:
          if i.variable.text not in usedvars:
            cfg.nodes[node]['instrs'].remove(i)

  return cfg


if len(sys.argv) > 1:
  # create a mapping from filenames to their input streams
  filepaths = sys.argv[1:]
  streams = { os.path.basename(filepath): FileStream(filepath) for filepath in filepaths }
else:
  # create a single mapping from stdin to the input stream
  input_stream = StdinStream()
  filename = "stdin"
  streams = { filename: input_stream }

# generate an interpreter for each function by running the listener
lexer = SimpleIRLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = SimpleIRParser(stream)
tree = parser.unit()
if parser.getNumberOfSyntaxErrors() > 0:
  print("syntax errors")
  exit(1)
walker = ParseTreeWalker()
irl = IRList()
walker.walk(irl, tree)
# print(irl.instr)
cfg = controlflow(irl.instr)
ocfg = deadCodeElimination(cfg)
getInstructions(ocfg)