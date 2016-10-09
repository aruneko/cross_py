# インストール先のディレクトリ
install_dir = '/usr/local/cross'
# アーカイブの保存先
orig_dir = 'orig/'
# 展開済みソースコードの保存先
src_dir = 'src/'
# ビルド用ディレクトリ
build_dir = 'build/'
# 各種ファイルのバージョン
files = { 'binutils': 'binutils-2.26.1',\
          'gcc'     : 'gcc-5.3.0' ,\
          'gdb'     : 'gdb-7.11.1',\
          'gmp'     : 'gmp-6.1.0' ,\
          'mpc'     : 'mpc-1.0.3' ,\
          'mpfr'    : 'mpfr-3.1.4'}
# GNUのミラーサイト(Jaistがデフォルト)
gnu_site = 'http://ftp.jaist.ac.jp/pub/GNU/'
# make時のオプション
makeopt = '-j9'
