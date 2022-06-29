#include "lists.h"

/**
 * insert_node - inserts a node into an orderly  linked list
 * @head: pointer to the pointer to the first node of the list
 * @number: number is the value to be added
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node, *temp, *prev;
	int loop = 0;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	while (current->next != NULL)
	{
		if (number > current->n)
		{
			loop = 1;
			prev = current;
			current = current->next;
		}
		else
		{
			if (loop == 0)
			{
				new_node->next = *head;
				*head = new_node;
			}
			else
			{
				temp = prev->next;
				prev->next = new_node;
				new_node->next = temp;
			}
			return (new_node);
		}
	}
	current->next = new_node;
	return (new_node);
}
