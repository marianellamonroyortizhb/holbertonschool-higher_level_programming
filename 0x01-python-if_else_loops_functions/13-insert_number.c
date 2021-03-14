#include "lists.h"

/**
 * insert_node - Insert a number
 * @head: Head element
 * @number: Counter
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *tmp, *ptr;

    ptr = malloc(sizeof(listint_t));
    if (!ptr)
        return (NULL);
    tmp = *head;
    ptr->n = number;
    if (!*head || tmp->n > number)
        return (ptr->next = *head, *head = ptr, ptr);
    while (tmp->next)
    {
        if (tmp->next->n >= number)
            return (ptr->next = tmp->next, tmp->next = ptr, ptr);
        tmp = tmp->next;
    }
    ptr->next = NULL;
    tmp->next = ptr;
    return (ptr);
}
