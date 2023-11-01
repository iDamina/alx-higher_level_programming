#include "lists.h"
/**
  *check_cycle - function to check if a singly linked
  *list has a cycle in it
  *@list: the list
  *Return: returns 0 if no cycle and 1 if there is cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL)
		return (0);

	fast = list;
	slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
