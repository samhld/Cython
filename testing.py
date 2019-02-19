
import timeit

cy = timeit.timeit('example_cy.test(5)', setup = 'import example_cy')
py = timeit.timeit('example_py.test(5)', setup = 'import example_py')

print('Cython program ran in: ' + str(cy) + " seconds")
print('Python program ran in: ' + str(py) + " seconds")
