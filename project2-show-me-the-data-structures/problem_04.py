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
    
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True

    return False

## Test cases
# Test Case 1: User in parent group
print("Test Case 1 - should return True")
print(is_user_in_group(sub_child_user, parent))

# Test Case 2: User in child group
print("Test Case 2 - should return True")
print(is_user_in_group(sub_child_user, child))

# Test Case 3: User in subchild group
print("Test Case 3 - should return True")
print(is_user_in_group(sub_child_user, sub_child))

# Test Case 4: User not found in subchild group
print("Test Case 4 - should return False")
print(is_user_in_group("test user", sub_child))

# Test Case 5: User not found in empty group
empty_group = Group("empty")
print("Test Case 5 - should return False")
print(is_user_in_group(sub_child_user, empty_group))

# Test Case 6: User has no parent
no_parent_group = Group("no_parent")
no_parent_group.add_user(sub_child_user)
print("Test Case 6 - should return True")
print(is_user_in_group(sub_child_user, no_parent_group))