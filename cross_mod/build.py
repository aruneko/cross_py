import cross_mod.config as conf
import os
import subprocess

class Buid:
  def __init__(self):
    self.build_target = 'gmp'
    self.opt = '--prefix=' + conf.install_dir
    if os.path.exists(conf.build_dir):
      os.mkdir(conf.build_dir)

  def build(self):
    os.mkdir(conf.build_dir + build_target)
    os.chdir(conf.build_dir + build_target)
    subprocess.run(['../../%s/%s/configure' \
                % (conf.src_dir, conf.files[self.build_target]), self.opt])
    subprocess.run(['make', conf.makeopt])
    subprocess.run(['make', conf.makeopt, 'check'])
