#include "lists.h"

/**
 * check_cycle - checks if linked list is circular
 * @list:linked list to be checked.
 * Return: 0 if not circular or 1 if circular.
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *list_temp;

	if (list == NULL)
		return (0);

	current = list->next;
	list_temp = list;
	while (current != NULL)
	{
		if (current == list_temp)
			return (1);
		current = current->next;
	}

	return (0);
}
