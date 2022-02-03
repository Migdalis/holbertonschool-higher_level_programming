#include "lists.h"

/**
 * insert_node - function in C that inserts a number into
 * a sorted singly linked list
 * @head: head of the sorted linked list
 * @number: value of the node to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *aux;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (!current || (current->n > new->n))
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current)
	{
		if ((current->n < new->n && current->next->n > new->n)
		|| current->n == new->n)
		{
			aux = current->next;
			current->next = new;
			new->next = aux;
			return (new);
		}
		current = current->next;
	}
	return (NULL);
}
