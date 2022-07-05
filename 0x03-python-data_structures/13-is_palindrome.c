#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *step;
	listint_t *current;

	int n = 0, k, i;

	if (*head == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	k = n / 2;
	step = *head;
	current = *head;
	while (k != 0)
	{
		for (i = 1; i < n; i++)
			step = step->next;
		if (current->n == step->n)
		{
			current = current->next;
			n = n - 2;
			step = current;
		}
		else
		{
			return (0);
		}
		k = k - 1;
	}
	return (1);
}
