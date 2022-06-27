#include "lists.h"

/**
 * check_cycle - checks if linked list is circular
 * @head: head of linked list
 * Return: 0 if not circular or 1 if circular.
 */
int check_cycle(listint_t *head)
{
	listint_t *current;

	if (head == NULL)
		return (0);
	current = head->next;
	while (current != NULL)
	{
		if (current == head)
			return (1);
		current = current->next;
	}
	return (0);
}
