#include "lists.h"

/**
 * reverse - reverses the linked list
 * @head: head of linked list
 * Return: void
 */

void reverse(listint_t **head)
{
	listint_t *temp;
	listint_t *current;
	listint_t *prev;

	current = *head;
	prev = NULL;
	while (current != NULL)
	{
		temp = current->next;
		current->next = prev;
		prev = current;
		current = temp;
	}
	*head = prev;
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *current2;

	if (*head == NULL)
		return (1);

	current = *head;
	current2 = *head;
	reverse(&current2);
	while (current != NULL)
	{
		if (current->n == current2->n)
		{
			current = current->next;
			current2 = current2->next;
		}
		else
			return (0);
	}
	return (1);
}
