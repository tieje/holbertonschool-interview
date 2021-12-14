#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * insert_node - insert number in singly linked list, l to g
 * @head: head of the singly linked list
 * @number: insert);
 * Return: address of new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *prev = *head;
	listint_t *current = prev->next;

	while (number > current->n)
	{
		prev = current;
		current = current->next;
		if (current == NULL)
		{
			return (add_nodeint_end(head, number));
		}
	};
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = current;
	prev->next = new;
	return (new);
}
