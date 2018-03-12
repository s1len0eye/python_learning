
from admin import Privileges, Admin

admin  = Admin('Bob', 'Black', location='Canada', job='worker')
admin.privileges.show_privileges()
