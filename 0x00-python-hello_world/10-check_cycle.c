#include "lists.h"

/**
 * check_cycle - checks if linked list is circular
 * @list:linked list to be checked.
 * Return: 0 if not circular or 1 if circular.
 */
int check_cycle(listint_t *list)
{
	listint_t *current1;
	listint_t *current2;

	if (list == NULL)
		return (0);

	current1 = list;
	current2 = list;

	while (current1->next && current2->next->next)
	{
		current1 = current1->next;
		current2 = current2->next->next;
		if (current1 == list)
			return (1);
		if (current1 == current2)
			return (1);
	}

	return (0);
}
