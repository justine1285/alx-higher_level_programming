#include "lists.h"
/**
 * is_palindrome - checks if a singly-linked list is a palidrome
 * @head: pointer to address of firdt node
 * Return: 1 if list is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int list_length = 0;

	if (!*head)
		return (1);

	temp = *head;
	while (temp)
	{
		list_length++;
		temp = temp->next;
	}
	if (list_length % 2 != 0)
		return (0);

	return (1);
}
