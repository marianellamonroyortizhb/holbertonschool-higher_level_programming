#include "lists.h"
/**
 * PalindromeRecur - Check if list is a palindrome.
 * @left: First node
 * @right: Last node.
 */
int palindrome(listint_t **left, listint_t *right)
{
	int pal;

	if (right == NULL)
		return (1);

	pal = palindrome(left, right->next);
	if (pal == 0)
		return (0);

	pal = (right->n == (*left)->n);

	*left = (*left)->next;
	return (pal);
}

/**
 * is_palindrome - Check if linked list is palindrome.
 * @head: List
 * @right: Last node
 */
int is_palindrome(listint_t **head)
{
	int res;

	if (!head)
		return (0);
	res = palindrome(head, *head);
	return (res);
}
