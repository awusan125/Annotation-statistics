import ast
path='/home/wzd/notebook/pycode/'
readfile=path+'test.txt'


# 由于一个变量往往只会用来表示一种类型
class CodeVisitor(ast.NodeVisitor):
    path = [[]]
    ann_arg = 0
    ann_ret = 0
    ann_ass = 0
    nan_arg = 0
    nan_ret = 0
    nan_ass = 0

    def generic_visit(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_FunctionDef(self, node):
        if (node.returns):
            self.ann_ret += 1
        else:
            self.nan_ret += 1

        t = []
        # 变量集中加入参数

        for k in node.args.args:
            t.append(k.arg)
            if k.annotation:
                self.ann_arg += 1
            else:
                self.nan_arg += 1

        # 变量集中加入返回值
        if type(node.body[-1]).__name__ == 'Return':  # 又return
            if type(node.body[-1].value).__name__ == 'Name':
                t.append(node.body[-1].value.id)

        self.path.append(t)
        ast.NodeVisitor.generic_visit(self, node)
        self.path.pop(-1)

    def visit_Assign(self, node):
        self.nan_ass += 1
        ast.NodeVisitor.generic_visit(self, node)

    def visit_AnnAssign(self, node):
        self.ann_ass += 1
        ast.NodeVisitor.generic_visit(self, node)


x = CodeVisitor()
f = open(readfile, 'r')
line = f.read().split('\n')
for i in line:
    if i:
        file = open(i, "r")
        source = file.read()
        root = ast.parse(source)
        x.visit(root)

# ast.fix_missing_locations(root)

# code_object = compile(root, "<string>", "exec")
# exec(code_object)

print('ann_arg:',x.ann_arg)
print('nan_arg:',x.nan_arg)
print('ann_ret:',x.ann_ret)
print('nan_ret:',x.nan_ret)
print('ann_ass:',x.ann_ass)
print('nan_ass:',x.nan_ass)
print('rate_arg:',x.ann_arg/(x.ann_arg+x.nan_arg))
print('rate_ret:',x.ann_ret/(x.ann_ret+x.nan_ret))
print('rate_ass:',x.ann_ass/(x.ann_ass+x.nan_ass))

print('ann_arg:',x.ann_arg)
print('nan_arg:',x.nan_arg)
print('ann_ret:',x.ann_ret)
print('nan_ret:',x.nan_ret)
print('ann_ass:',x.ann_ass)
print('nan_ass:',x.nan_ass)
print('rate_arg:',x.ann_arg/(x.ann_arg+x.nan_arg))
print('rate_ret:',x.ann_ret/(x.ann_ret+x.nan_ret))
print('rate_ass:',x.ann_ass/(x.ann_ass+x.nan_ass))
