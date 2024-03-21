# -*- coding: utf-8 -*-
# 完成数据库的查询 以及返回结果
from py2neo import Graph, Node, Relationship, NodeMatcher

class Data2Neo4j:
    def __init__(self, url, username, password):
        self.graph = Graph(url, user=username, password=password)
        self.matcher = NodeMatcher(self.graph)

    def create_node(self, label, name):
        node = Node(label, name=name)
        self.graph.create(node)

    def create_relation(self,label, head, tail, relation):
        try:
            head_node = self.matcher.match(label,name=head).first()
            tail_node = self.matcher.match(label,name=tail).first()
            self.graph.create(Relationship(head_node, relation, tail_node))
        except:
            raise Exception("Node not found")

    def query(self, query):
        return self.graph.run(query)


    def revise_add_node(self, label, name,new_property):
        node = self.matcher.match(label, name=name).first()
        node["name"]=new_property
        self.graph.push(node)

    def delete_all(self):
        self.graph.delete_all()

    def print_all(self):
        result = self.query("MATCH (n) RETURN n")

        for i in result:
            print(i)