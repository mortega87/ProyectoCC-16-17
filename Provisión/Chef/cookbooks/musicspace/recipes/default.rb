apt_update 'all platforms'

package 'git'
package 'mongodb'
package 'python-setuptools'
package 'python-dev'
package 'python-pip'

execute 'PyMongo' do
  command 'pip install pymongo'
end

execute 'Python' do
  command 'pip install python'
end

execute 'Virtualenv' do
  command 'pip install virtualenv'
end

execute 'Django' do
  command 'pip install django'
end
