#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *jump;

	if (!list)
		return (0);
	temp = list->next;
	jump = temp->next;
	while (temp && jump && jump->next)
	{
		if (temp == jump)
			return (1);
		temp = temp->next;
		jump = jump->next->next;
	}
	return (0);
}
