#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task_01-05"""


import time


class ChessPiece(object):
    """Chess game positions. """
    prefix = ''

    def __init__(self, position):
        """Constructor for the ChessPiece() class.

        Args:
            position (string): Position on the chess board.

        Attributes:
            position (string): Position on the chess board.
        """
        if not self.is_legal_move(position):
            excep = '{0} is not a legal start position'
            raise ValueError(excep.format(position))

        self.position = position
        self.moves = []

    def algebraic_to_numeric(self, tile=None):
        """This function converts string into integers

        Args:
            tile (str): Chess position. Default is None.

        Returns:
            bool, int: Converted string argument into integer. If else return Fa
            lse.

        Examples:

            >>> obj = ChessPiece('a1')
            >>> obj.algebraic_to_numeric('a1')
            (0, 0)
        """
        my_x = tile[0]
        my_y = tile[1]
        if ord(my_x) < 96 or int(my_y) < 1 or ord(my_x) > 104 or int(my_y) > 8:
            return None

        my_x = ord(my_x) - 97
        my_y = int(my_y) - 1
        return (my_x, my_y)

    def is_legal_move(self, position):
        """Function determines if chess move is legal.

        Args:
            position(str): Input of position by user.

        Returns:
            bool: True if argument is on chess board, False if argument is out o
            f chess board.

        Examples:

            >>> obj = ChessPiece('a1')
            >>> obj.is_legal_move('a1')
            True
        """
        if self.algebraic_to_numeric(position) is None:
            return False
        else:
            return True

    def move(self, position):
        """Function saves positions and determine if new position is legal.

        Args:
            position(int): numeric input postion.

        Returns:
            mixed: tuple of legal positons taken before. If else returns False.
            Also includes time of the move.

        Examples:

            >>> obj = ChessPiece('a1')
            >>> obj.move('a2')
            ('a1', 'a2', 1478483602.258554)
        """
        if not self.is_legal_move(position):
            return False
        oldposition = self.position
        self.position = position
        self.moves.append(((self.prefix + oldposition, self.prefix +
                            self.position, time.time())))
        return self.moves[len(self.moves) - 1]


class Rook(ChessPiece):
    """Rook moves"""
    prefix = 'R'

    def __init__(self, position):
        """Constructor for the Rook() class.

        Args:
            position (str): User input of chess position.

        Attributes:
            position (str): User input of chess position.
        """
        ChessPiece.__init__(position)
        self.position = position
        self.moves = []

    def is_legal_move(self, position):
        """Function determines if chess move is legal.

        Args:
            position(str): Input of position by user.

        Returns:
            bool: True if argument is making right move, False if argument is no
            t.

        Examples:

            >>> obj = Rook('a1')
            >>> obj.is_legal_move('a2')
            True
        """
        if ChessPiece.is_legal_move(self, position):
            if (self.position[0] != position[0] and
                    self.position[1] != position[1]):
                return False
            else:
                return True
        return False

    def move(self, position):
        """Function determine if Rook position is legal.

        Args:
            position(int): numeric input postion.

        Returns:
            mixed: tuple of legal positons taken before. If else returns False.
            Also includes time of the move.

        Examples:

            >>> obj = ChessPiece('a1')
            >>> obj.move('a2')
            ('a1', 'a2', 1478483602.258554)
        """
        if not self.is_legal_move(position):
            return False
        oldposition = self.position
        self.position = position
        self.moves.append(((self.prefix + oldposition, self.prefix +
                            self.position, time.time())))
        return self.moves[len(self.moves) - 1]


class Bishop(ChessPiece):
    """Bishop moves"""
    prefix = 'B'

    def __init__(self, position):
        """Constructor for the Bishop() class.

        Args:
            position (str): User input of chess position.

        Attributes:
            position (str): User input of chess position.
        """
        ChessPiece.__init__(position)
        self.position = position
        self.moves = []

    def is_legal_move(self, position):
        """Function determines if Bishop chess move is legal.

        Args:
            position(str): Input of position by user.

        Returns:
            bool: True if argument is making legal move, False if argument is no
            t.

        Examples:

            >>> obj = Bishop('a1')
            >>> obj.is_legal_move('b2')
            True
        """
        pos_new = ChessPiece.algebraic_to_numeric(self, position)
        pos_old = ChessPiece.algebraic_to_numeric(self, self.position)
        if ChessPiece.is_legal_move(self, position):
            if abs(pos_new[0] - pos_old[0]) == abs(pos_new[1] - pos_old[1]):
                return True
            else:
                return False
        return False

    def move(self, position):
        """Function determine if Bishop position is legal.

        Args:
            position(int): numeric input postion.

        Returns:
            mixed: tuple of legal positons taken before. If else returns False.
            Also includes time of the move.

        Examples:

            >>> obj = Bishop('a1')
            >>> obj.move('b2')
            ('Ba1', 'Bb2', 1478486001.661696)
        """
        if not self.is_legal_move(position):
            return False
        oldposition = self.position
        self.position = position
        self.moves.append(((self.prefix + oldposition, self.prefix +
                            self.position, time.time())))
        return self.moves[len(self.moves) - 1]


class King(ChessPiece):
    """King moves"""
    prefix = 'K'

    def __init__(self, position):
        """Constructor for the King() class.

        Args:
            position (str): User input of chess position.

        Attributes:
            position (str): User input of chess position.
        """
        ChessPiece.__init__(position)
        self.position = position
        self.moves = []

    def is_legal_move(self, position):
        """Function determines if King chess move is legal.

        Args:
            position(str): Input of position by user.

        Returns:
            bool: True if argument is making legal move, False if argument is no
            t.

        Examples:

            >>> obj = King('c3')
            >>> obj.is_legal_move('c2')
            True
        """
        pos_new = ChessPiece.algebraic_to_numeric(self, position)
        pos_old = ChessPiece.algebraic_to_numeric(self, self.position)
        if ChessPiece.is_legal_move(self, position):
            if (abs(pos_new[0] - pos_old[0]) == 1 and
                    abs(pos_new[1] - pos_old[1]) == 1 or
                    (abs(pos_old[0] - pos_new[0]) == 1 or
                     abs(pos_old[1] - pos_new[1])) == 1):
                return True
            else:
                return False
        return False

    def move(self, position):
        """Function determine if King position is legal.

        Args:
            position(int): numeric input postion.

        Returns:
            mixed: tuple of legal positons taken before. If else returns False.
            Also includes time of the move.

        Examples:

            >>> obj = King('c3')
            >>> obj.move('c2')
            ('Kc3', 'Kc2', 1478486324.737411)
        """
        if not self.is_legal_move(position):
            return False
        oldposition = self.position
        self.position = position
        self.moves.append(((self.prefix + oldposition, self.prefix +
                            self.position, time.time())))
        return self.moves[len(self.moves) - 1]


class ChessMatch(object):
    """Matching chess positions."""
    def __init__(self, pieces=None):
        """Constructor for ChessMatch() class.

        Args:
            pieces(dict): dictionary of chess position. Default: None.

        Attributes:
            pieces(dict): dictionary of chess position. Default: None.
        """
        if pieces is not None:
            self.pieces = pieces
            self.log = []
        else:
            self.pieces = {}
            self.log = []
            self.reset()

    def reset(self):
        """Function to erase dictionary for each new match."""
        del self.log[:]
        self.pieces = {'Ra1': Rook('a1'),
                       'Rh1': Rook('h1'),
                       'Ra8': Rook('a8'),
                       'Rh8': Rook('h8'),
                       'Bc1': Bishop('c1'),
                       'Bf1': Bishop('f1'),
                       'Bc8': Bishop('c8'),
                       'Bf8': Bishop('f8'),
                       'Ke1': King('e1'),
                       'Ke8': King('e8')}

    def move(self, m_long, m_short):
        """Function collects all game logs

        Args:
            m_long(str): input value with prefix.
            m_short(str): input value.

        Returns:
            tuple: collection of moves in tuple with time of it.

        Examples:

            >>> obj = ChessMatch({'Ra1': Rook('a1')})
            >>> obj.move('Ra1','a2')
            >>> obj.log
            [('Ra1', 'Ra2', 1478487710.885655)]
        """
        if self.pieces[m_long].is_legal_move(m_short) is False:
            return False
        else:
            self.log.append(self.pieces[m_long].move(m_short))
            key = self.pieces[m_long].prefix + m_short
            value = self.pieces.pop(m_long)
            self.pieces[key] = value
