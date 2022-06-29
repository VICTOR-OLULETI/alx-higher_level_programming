#include "lists.h"

/**
 * insert_node - inserts a node into an orderly  linked list
 * @head: pointer to the pointer to the first node of the list
 * @number: number is the value to be added
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new_node;
	listint_t *temp;
	listint_t *prev;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
		*head = new_node;

	while (current != NULL)
	{
		if (number > current->n)
		{
			prev = current;
			current = current->next;
		}
		else
		{
			temp = prev->next;
			prev->next = new_node;
			new_node->next = temp;
			break;
		}
	}
	return (new_node);
}
