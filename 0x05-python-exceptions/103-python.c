#include <Python.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size, allocated, i;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = Py_SIZE(list);
	allocated = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; ++i)
	{
		printf("Element %zd: ", i);
		PyObject_Print(PyList_GetItem(p, i), stdout, 0);
		printf("\n");
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size, i;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_GET_SIZE(bytes);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first 10 bytes: ");
	for (i = 0; i < 10 && i < size; ++i)
	{
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(bytes)[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to a Python object
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *float_obj = (PyFloatObject *)p;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %lf\n", float_obj->ob_fval);
}
