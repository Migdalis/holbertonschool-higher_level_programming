#include "lists.h"

/**
 * reverse_listint - Function that reverses a linked list
 * @head: Head of a list
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = NULL, *aux;

	if (head == NULL || *head == NULL)
		return (NULL);
	if ((*head)->next == NULL)
		return (*head);
	while (*head)
	{
		aux = (*head)->next;
		(*head)->next = next;
		next = aux->next;
		aux->next = *head;
		*head = next;
		next = aux;
	}

	*head = next;
	return (*head);
}

/**
 * listint_len - Function that returns the number of elements in a linked list
 * @h: Head of a list
 * Description: Function that returns the number of elements in a linked list
 * Return: The number of nodes
 */
size_t listint_len(const listint_t *h)
{
	size_t count = 0;

	while (h)
	{
		count++;
		h = h->next;
	}
	return (count);
}

/**
 *is_palindrome - Test a list
 *@head: List to test
 *Description: Function that test if a list is palindrome or not
 *Return: 1 if the list is a palindrome and 0 if not
 *
 **/
int is_palindrome(listint_t **head)
{
	int len, i = 0;
	listint_t *rev_list;

	len = listint_len(*head);
	if (len == 0)
		return (1);
	rev_list = reverse_listint(head);
	while (i < (len / 2) - 1)
	{
		if (rev_list->n != (*head)->n)
			return (0);
		i++;
		rev_list = rev_list->next;
		*head = (*head)->next;
	}
	return (1);
}
