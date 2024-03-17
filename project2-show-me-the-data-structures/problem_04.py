class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    if user in group.get_users():
        return True
    
    for group in group.get_groups():
        return is_user_in_group(user, group)

    return False

## Test cases
print("Test Case 1 - should return True")
print(is_user_in_group(sub_child_user, parent))

print("Test Case 2 - should return True")
print(is_user_in_group(sub_child_user, child))

print("Test Case 3 - should return True")
print(is_user_in_group(sub_child_user, sub_child))

print("Test Case 4 - should return False")
print(is_user_in_group("test user", sub_child))