import cross_mod.config as conf
import shutil
import urllib.request
import os
import hashlib
import subprocess

class ToolChain:
  def __init__(self):
    # ダウンロードするファイル(圧縮形式がバラバラなのがやっかい)
    self.files = [conf.files['binutils'] + '.tar.bz2', \
                  conf.files['gcc']      + '.tar.bz2', \
                  conf.files['gdb']      + '.tar.xz' , \
                  conf.files['gmp']      + '.tar.xz' , \
                  conf.files['mpfr']     + '.tar.bz2', \
                  conf.files['mpc']      + '.tar.gz']

  def download(self):
    # ダウンロード先のパスの形式を作成(gccだけ例外なのがやっかい)
    fpaths = ['binutils/', \
              'gcc/%s/' % conf.files['gcc'], \
              'gdb/' , \
              'gmp/' , \
              'mpfr/', \
              'mpc/']
    # パスとファイル名を結合
    dl_paths = [p + f for p, f in zip(fpaths, self.files)]
    # ダウンロード先ディレクトリの作成
    if not os.path.exists(conf.orig_dir):
      os.mkdir(conf.orig_dir)
    # ダウンロードの実行
    for p, f in zip(dl_paths, self.files):
      if os.path.exists(conf.orig_dir + f):
        print('%s is exists. skip download.' % f)
      else:
        print('downloading %s ...' % f)
        urllib.request.urlretrieve(conf.gnu_site + p, conf.orig_dir + f)
        print('done!')

  def checksum(self):
    # チェックサム辞書の作成
    sums = ['d2b24e5b5301b7ff0207414c34c3e0fb',\
            'c9616fd448f980259c31de613e575719',\
            '5aa71522e488e358243917967db87476',\
            'a9868ef2556ad6a2909babcd1428f3c7',\
            'b8a2f6b0e68bef46e53da2ac439e1cf4',\
            'd6a1d5f8ddea3abd2cc3e98f58352d26']
    sum_dict = {f:s for f, s in zip(self.files, sums)}
    # チェックサムの実施
    for f, s in sum_dict.items():
      with open(conf.orig_dir + f, 'rb') as t:
        if hashlib.md5(t.read()).hexdigest() == s:
          print('%s is OK.' % f)
        else:
          print('ERROR %s has bad checksum.' % f)

  def setup(self):
    # 展開先ディレクトリの作成
    if not os.path.exists(conf.src_dir):
      os.mkdir(conf.src_dir)
    # 展開の実施
    for f in self.files:
      subprocess.run(['tar', 'xvf', conf.orig_dir + f, '-C', conf.src_dir])

  def clean(self):
    # 展開先ディレクトリの中身をすべて消去
    for f in conf.files:
      shutil.rmtree(conf.src_dir + f)
