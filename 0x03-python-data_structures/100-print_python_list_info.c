#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info - Info list.
 * @p: List.
 * Return: None.
 */

void print_python_list_info(PyObject *p)
{
	int alloc, i = 0;
	int len;
	PyObject *obj;

	len = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloc);

	while (i < len)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		i++;
	}
}
