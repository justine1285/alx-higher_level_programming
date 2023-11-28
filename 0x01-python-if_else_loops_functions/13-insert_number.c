#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"
/**
 * insert_node - insert a number into a list
 * @head: linked list
 * @number: number to be inserted
 * Return: pointer to the new head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *present = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (present && present->n < number)
		{
			temp = present;
			present = present->next;
		}

		temp->next = new;
		new->next = present;
	}
	return (new);
}
