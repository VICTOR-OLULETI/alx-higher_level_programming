#include "lists.h"

/**
 * reverse - reverses the linked list
 * @head: pointer to pointer to head
 * Return: void
 */

void reverse(listint_t **head)
{
	listint_t *temp, *curr, *prev;

	curr = *head;
	prev = NULL;
	while (curr != NULL)
	{
		temp = curr->next;
		curr->next = prev;
		prev = curr;
		curr = temp;
	}
	*head = prev;
}

/**
 * compareLists - checks the input data for each linked list
 * @head1: head of first list
 * @head2: head of second list
 * Return: 1 if the same data is present in each list else  0.
 */

bool compareLists(listint_t *head1, listint_t *head2)
{
	listint_t *h1 = head1;
	listint_t *h2 = head2;


	while (h1 && h2)
	{
		if (h1->n == h2->n)
		{
			h1 = h1->next;
			h2 = h2->next;
		}
		else
		{
			return (0);
		}
	}
	if (h1 == NULL && h2 == NULL)
		return (1);
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;
	listint_t *second_half, *prev_slow_ptr = *head;
	listint_t *middlenode = NULL;
	bool res = true;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		if (fast_ptr != NULL)
		{
			middlenode = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		second_half = slow_ptr;
		prev_slow_ptr->next = NULL;
		reverse(&second_half);
		res = compareLists(*head, second_half);

		reverse(&second_half);

		if (middlenode != NULL)
		{
			prev_slow_ptr->next = middlenode;
			middlenode->next = second_half;
		}
		else
		{
			prev_slow_ptr->next = second_half;
		}
	}
	return (res);
}
