'''Build below location tree using TreeNode class
Now modify print_tree method to take tree level as input. And that should print tree only upto that level as shown below,'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level):
        spaces = " "*self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                if level == self.get_level():
                    break
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_location_tree():
    root = TreeNode("Global")

    gujrat = TreeNode("Gujrat")
    gujrat.add_child(TreeNode("Ahmedabad"))
    gujrat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangalore"))
    karnataka.add_child(TreeNode("Mysore"))

    india = TreeNode("India")
    india.add_child(gujrat)
    india.add_child(karnataka)

    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa = TreeNode("USA")
    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    root.print_tree(3)
    root.print_tree(2)
    root.print_tree(1)

if __name__ == '__main__':
    build_location_tree()