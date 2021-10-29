import os
try:
  import chess
  import chess.svg
except ModuleNotFoundError:
  os.system("pip install chess")
  import chess
  import chess.svg
os.system("clear")
class Chess():
  Board,turn,kingsmoved,rooksmoved,castled,enpassant,push_or_take,movecount,fenregister=[[-49,-29,-32,-90,-2000,-32,-29,-50],[-10,-10,-10,-10,-10,-10,-10,-10],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[10,10,10,10,10,10,10,10],[49,29,32,90,2000,32,29,50]],True,[False,False],[False,False,False,False],[False,False],None,0,0,[];
  piece={
    "0":"□",
    "-2000":"k", #black king
    "-90":"q", #black queen
    "-50":"r", #black king rook
    "-49":"r", #black queen rook
    "-32":"b", #black bishop
    "-29":"n", #black knight
    "-10":"p", #black 
    "10":"P", #white 
    "29":"N", #white knight
    "32":"B", #white bishop
    "49":"R", #white rook
    "50":"R", #white rook
    "90":"Q", #white queen
    "2000":"K", #white king
    "k":-2000, #black king
    "q":-90, #black queen
    "r":-49, #black queen's rook
    "b":-32, #black bishop
    "n":-29, #black knight
    "p":-10, #black 
    "P":10, #white 
    "N":29, #white knight
    "B":32, #white bishop
    "R":49, #white queen's rook
    "Q":90, #white queen
    "K":2000, #white king
  }
  def UCI_to_NCN(self,uci,a={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}): 
    if len(uci)==4:
      return ((8-int(uci[1]),a[uci[0]]),(8-int(uci[3]),a[uci[2]]),"")
    else:
      return ((8-int(uci[1]),a[uci[0]]),(8-int(uci[3]),a[uci[2]]), (self.piece[uci[4].upper()] if self.turn else self.piece[uci[4]]))
  def NCN_to_UCI(self,ncn,promotion="",a={0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h"}):
    uci=str(f"{a[8-ncn[0][1]]}{8-ncn[0][0]}{a[8-ncn[1][1]]}{8-ncn[1][0]}{promotion.lower()}")
    return uci
  def push(self,uci=None,move=None):
    n=self.get_fen()
    self.fenregister.append(n)
    if move==None and uci==None:
      c=self.legalMoves(n)
      mov=str(input("Enter UCI move: "))
      while not mov in c:
        mov=str(input("Enter UCI move: "))
      move=self.UCI_to_NCN(mov)
      del c, mov
    elif move==None and uci!=None:
      move=self.UCI_to_NCN(uci)
    piece=self.Board[move[0][0]][move[0][1]]
    b=self.Board[move[1][0]][move[1][1]]
    if piece==10 and move[0][0]==6 and move[1][0]==4:
      enp=self.NCN_to_UCI(move)
      self.enpassant=enp[0]+str(int(enp[1])+1)
    elif piece==-10 and move[0][0]==1 and move[1][0]==3:
      enp=self.NCN_to_UCI(move)
      self.enpassant=enp[0]+str(int(enp[1])+1)
    if piece in (10,-10):
      self.push_or_take=0
    elif b!=0:
      self.push_or_take+=1
    if piece==2000:
      self.kingsmoved[0]=True
    elif piece==-2000:
      self.kingsmoved[1]=True
    elif move[0]==[7,7]:
      self.rooksmoved[0]=True
    elif move[0]==[7,0]:
      self.rooksmoved[1]=True
    elif move[0]==[0,7]:
      self.rooksmoved[0]=True
    elif move[0]==[0,0]:
      self.rooksmoved[0]=True
    if move[2]!="":
      piece=move[2]
    self.Board[move[0][0]][move[0][1]]=0
    self.Board[move[1][0]][move[1][1]]=piece
    if self.turn:
      self.turn=False
    else:
      self.turn=True

  def show(self,mode=None):
    if mode==None:
      print(f"{self.piece[str(self.Board[0][0])]} {self.piece[str(self.Board[0][1])]} {self.piece[str(self.Board[0][2])]} {self.piece[str(self.Board[0][3])]} {self.piece[str(self.Board[0][4])]} {self.piece[str(self.Board[0][5])]} {self.piece[str(self.Board[0][6])]} {self.piece[str(self.Board[0][7])]}\n{self.piece[str(self.Board[1][0])]} {self.piece[str(self.Board[1][1])]} {self.piece[str(self.Board[1][2])]} {self.piece[str(self.Board[1][3])]} {self.piece[str(self.Board[1][4])]} {self.piece[str(self.Board[1][5])]} {self.piece[str(self.Board[1][6])]} {self.piece[str(self.Board[1][7])]}\n{self.piece[str(self.Board[2][0])]} {self.piece[str(self.Board[2][1])]} {self.piece[str(self.Board[2][2])]} {self.piece[str(self.Board[2][3])]} {self.piece[str(self.Board[2][4])]} {self.piece[str(self.Board[2][5])]} {self.piece[str(self.Board[2][6])]} {self.piece[str(self.Board[2][7])]}\n{self.piece[str(self.Board[3][0])]} {self.piece[str(self.Board[3][1])]} {self.piece[str(self.Board[3][2])]} {self.piece[str(self.Board[3][3])]} {self.piece[str(self.Board[3][4])]} {self.piece[str(self.Board[3][5])]} {self.piece[str(self.Board[3][6])]} {self.piece[str(self.Board[3][7])]}\n{self.piece[str(self.Board[4][0])]} {self.piece[str(self.Board[4][1])]} {self.piece[str(self.Board[4][2])]} {self.piece[str(self.Board[4][3])]} {self.piece[str(self.Board[4][4])]} {self.piece[str(self.Board[4][5])]} {self.piece[str(self.Board[4][6])]} {self.piece[str(self.Board[4][7])]}\n{self.piece[str(self.Board[5][0])]} {self.piece[str(self.Board[5][1])]} {self.piece[str(self.Board[5][2])]} {self.piece[str(self.Board[5][3])]} {self.piece[str(self.Board[5][4])]} {self.piece[str(self.Board[5][5])]} {self.piece[str(self.Board[5][6])]} {self.piece[str(self.Board[5][7])]}\n{self.piece[str(self.Board[6][0])]} {self.piece[str(self.Board[6][1])]} {self.piece[str(self.Board[6][2])]} {self.piece[str(self.Board[6][3])]} {self.piece[str(self.Board[6][4])]} {self.piece[str(self.Board[6][5])]} {self.piece[str(self.Board[6][6])]} {self.piece[str(self.Board[6][7])]}\n{self.piece[str(self.Board[7][0])]} {self.piece[str(self.Board[7][1])]} {self.piece[str(self.Board[7][2])]} {self.piece[str(self.Board[7][3])]} {self.piece[str(self.Board[7][4])]} {self.piece[str(self.Board[7][5])]} {self.piece[str(self.Board[7][6])]} {self.piece[str(self.Board[7][7])]}\n\n")
    if mode==0:
      print(str(chess.svg.board(chess.Board(self.get_fen()), size=350)),file=open("board.svg", "w"))
  def get_fen(self, board=None):
    if board==None:
      board=self.Board
    fen=""
    n=8
    for i in board:
      k=0
      b=False
      for j in i:
        if b and j==0:
          k+=1
        elif b:
          fen+=str(k)+self.piece[str(j)] 
          k=0
          b=False
        elif j==0:
          k=1
          b=True
        else:
          fen+=self.piece[str(j)] 
      if b:
        fen+=str(k)
      n-=1
      if n>0:
        fen+="/"
    if self.turn:
      fen+=" w "
    else:
      fen+=" b "
    if self.kingsmoved[0] or (self.rooksmoved[0] and self.rooksmoved[1]) or self.castled[0]:
      wk=""
    elif self.rooksmoved[0]:
      wk="K"
    elif self.rooksmoved[1]:
      wk="Q"
    else:
      wk="KQ"
    if self.kingsmoved[1] or (self.rooksmoved[2] and self.rooksmoved[3]) or self.castled[1]:
      bk=""
    elif self.rooksmoved[2]:
      bk="k"
    elif self.rooksmoved[3]:
      bk="q"
    else:
      bk="kq"
    kk=wk+bk+" "
    if kk==" ":
      if self.enpassant==None:
        fen+=f"-- {self.push_or_take} {self.movecount}"
      else:
        fen+=f"- {self.enpassant} {self.push_or_take} {self.movecount}"
    else:
      if self.enpassant==None:
        fen+=f"{kk}- {self.push_or_take} {self.movecount}"
      else:
        fen+=f"{kk}{self.enpassant} {self.push_or_take} {self.movecount}"
    return str(fen)
  def legalMoves(self,fen=None): 
    if fen==None:
      fen=self.get_fen()
    return [str(i) for i in chess.Board(fen).generate_legal_moves()]
  def gamestatus(self, fen=None):
    if fen==None:
      fen=self.get_fen()
    a=chess.Board(fen)
    if "w" in fen:
      turn=True
    else:
      turn=False
    if a.is_variant_loss():
      return (True,False,turn)
    elif a.is_variant_win():
      return (True,True,turn)
    elif self.push_or_take>=50:
      return (True,None,turn)
    else:
      del a
      b=self.halfen(fen)
      n=0
      for i in self.fenregister:
        if b == self.halfen(i):
          n+=1
        if n>=2:
          return (True,None,turn)
      return (False,None)
  def halfen(self, fen):
    half=""
    for i in fen:
      if i==" ":
        return half
      else:
        half+=i
  def score(self,board=None):
    if board==None:
      board=self.Board
    a=self.gamestatus(self.get_fen(board))
    if a[0]:
      if a[1]==None:
        if a[2]:
          return -2
        else:
          return 2
      elif a[1]:
        if a[2]:
          return 4000
        else:
          return -4000
      else:
        if a[2]:
          return -4000
        else:
          return 4000
    else:
      return sum(sum(i) for i in board)
