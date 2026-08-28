# a = 3;
# b = 3.14;
# c = 'abc';
# d = [ a, b, c ];
# e = ( a, b );
# # print( d );
# # abc
# '''
#     abc
# '''
# f = True;
# g = False;
# print( '%s%s'% ('a', 'b') )
# if( 1+ 1 == 2 ):
#     print( 'fuck' );
# while True:
#     print( 'fuck' );
# a = [ 'a', 'b', 'c' ];
# a = ( 'a', 'b', 'c' );
# a = { 'aa': 1, 'bb': 2 }
# for item in a:
#     print( a[ item ] );
# print( range( 5 ) );
# print( type( a ) );
# print( c.encode().decode() );
# print( c.find( 'c' ) );
# print( c* 2 );
# print( c[ 0 ] );
# print( c[ 0: 2 ] );
# print( 'a' in c );
# print( c.count( 'a' ) );
# print( c.index( 'f' ) );
# arr = [ 'a', 'b', 'c' ];
# arr.append( 'd' );
# print( arr );
# items = { 3, 1, 5, 2, 4 }
# print( type( items ) )
# items = { 'a', 'b', 'c', 'd' }
# items.discard( 'a' );
# print( items );
# def test( *args ):
#     print( args );
# test( 'fuck1', 'fuck2', 'fuck3' );
# def test( **args ):
#     print( args );
# test( fuck1 = 1, fuck2 = 2, fuck3 = 3 );
# def test():
#     def test2():
#         print( 'yes' );
#     test2();
# a = lambda: 'fuck';
# print( a() );
# import builtins;
# print( dir( builtins ) );
# a, b, c, d = ( 1, 2, 3, 4 );
# def test( *args ):
#     print( args );
# b, *a = ( 1, 2, 3, 4 );
# test( a );
# print( __name__ );
# def test():
#     return 1 if 2> 1 else 2;
# print( test() );

# def log1( func ):
#     def wrapper( *args, **kwargs ):
#         print( 'log1' );
#         result = func( *args, **kwargs );
#         print( 'log1' );
#         return result;
#     return wrapper;


# def log( func ):
#     def wrapper( *args, **kwargs ):
#         print( 'log' );
#         result = func( *args, **kwargs );
#         print( 'log' );
#         return result;
#     return wrapper;

# @log1
# @log
# def test( a, b ):
#     print( 'fuck:%s%s'% ( a, b ) );

# test( 'a', 'b' );

# class A:
#     height = 100;
#     def __init__( self ):
#         pass;

#     def test( self ):
#         print( self.height )

# A.height = 200;
# tt = A();
# tt.test();
# class B:
#     width = 50;
#     __width = 99;
#     _ne = 'wo';

#     def test( self ):
#         print( self.width );


# pe = B();
# # print( pe._B__width );
# pe._ne = 'ta'
# print( dir( object ) );

