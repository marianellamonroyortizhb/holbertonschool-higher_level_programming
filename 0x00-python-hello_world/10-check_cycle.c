#include "lists.h"

/**
 * check_cycle - Check a singly linked list
 * @list: List
 * Return: Always
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;


	if (!list)
		return (0);

	while (list != NULL)
	{
		ptr = list;
		list = list->next;
		if (ptr <= list)
			return (1);
	}
	return (0);

}
