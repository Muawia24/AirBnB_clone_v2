# Puppet for setup
exec {'sudo apt-get update':
  command => '/usr/bin/env apt-get -y update',
}
-> exec { 'nginx install':
  command => '/usr/bin/env apt-get -y install nginx',
}
-> exec { 'mkdir 1':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/',
}
-> exec {'mkdir 2':
  command => '/usr/bin/env mkdir -p /data/web_static/shared/',
}
-> exec {'index.html':
  command => '/usr/bin/env echo "Holberton School" > /data/web_static/releases/test/index.html',
}
-> exec {'symbolic-link':
  command => '/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current',
}
-> exec {'ownership':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data',
}
-> exec {'nginx-conf':
  command => '/usr/bin/env sed -i "47 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}" /etc/nginx/sites-available/default',
}
-> exec {'nginx-restart':
  command => '/usr/bin/env service nginx restart',
}
