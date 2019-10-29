#include <stdio.h>
#include <stdlib.h>

typedef struct adjnode 
{
	/* data */
	int data;
	struct adjnode* next;
}Node;

typedef struct list
{
	Node* head;
}List;

typedef struct graph
{
	/* data */
	int x;
	List* arr[];
}Graph;

List* addNode(int val)
{
	Node* fresh=(Node*)malloc(sizeof(Node));
	fresh->data=val;
	fresh->next=NULL;
	return fresh;
}

Graph* createGraph(int val)
{
	Graph* G=(Graph*)malloc(sizeof(Graph));
	G->x=val;
	G->arr=(List*)malloc(sizeof(List));
	for(int i=0;i<val;++i)
		G->arr[i]->head=NULL;
	return G;
}

void addEdge(Graph* G, int src, int dest)
{
	Node* new=addNode(dest);
	new->next=G->arr[src]->head;
	G->arr[src]->head=new;
	new=addNode(src);
	new->next=G->arr[dest]->head;
	G->arr[dest]->head=new;	
}
