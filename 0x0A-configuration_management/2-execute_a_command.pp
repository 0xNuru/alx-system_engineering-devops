# create a manifest that kills a process
# using pkill with puppet

exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
}
