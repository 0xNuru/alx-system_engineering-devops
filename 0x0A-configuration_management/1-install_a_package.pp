# This puppet manifest installs flask from pip3

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}
