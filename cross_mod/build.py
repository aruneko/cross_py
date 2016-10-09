import cross_mod.config as conf
import os
import subprocess

class Build:
  def __init__(self, target, opt):
    self.build_target = target
    self.opt = ['--prefix=' + conf.install_dir]
    if opt != []:
      self.opt = self.opt + opt
    if not os.path.exists(conf.build_dir):
      os.mkdir(conf.build_dir)

  def build(self):
    os.mkdir(conf.build_dir + self.build_target)
    os.chdir(conf.build_dir + self.build_target)
    subprocess.run(['../../%s%s/configure' \
                % (conf.src_dir, conf.files[self.build_target])] + self.opt)
    subprocess.run(['make', conf.makeopt])
    subprocess.run(['make', conf.makeopt, 'check'])
    subprocess.run(['make', 'install'])
    os.chdir('../../')

def build_deps():
  targets = ['gmp', 'mpfr', 'mpc']
  opts = [[], \
          ['--with-gmp=%s' % conf.install_dir, '--disable-thread-safe'], \
          ['--with-gmp=%s' % conf.install_dir, '--with-mpfr=%s' % conf.install_dir]]
  for t, o in zip(targets, opts):
    Build(t, o).build()
