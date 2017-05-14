class CalcCommand(filterpipes.FilterPipesCommandBase):

    def filter(self, data):
        expr = data.split('=')[0].strip(' ')
        math_expr = ''.join([c for c in expr.rstrip('*') if c in '0123456789+-/*,.()'])
        return '%s = %.2f' % (expr, eval(math_expr))