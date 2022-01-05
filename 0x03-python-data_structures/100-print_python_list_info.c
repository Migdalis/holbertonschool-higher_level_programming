#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i = 0;
	PyObject *list;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	while(i < size)
	{
		printf("Element %d: ", i);

		list = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(list)->tp_name);
		i++;
	}
}
