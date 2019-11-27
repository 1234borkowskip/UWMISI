using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
        
        }
        class Node
        {
            public int wartosc;
            public Node(int wartosc)
            {
                this.wartosc = wartosc;
            }
            public override string ToString()
            {
                return this.wartosc.ToString();
            }
        }
        class Krawedz
        {
            public Node start;
            public Node koniec;
            public int waga;
            public Krawedz(Node start, Node koniec, int waga)
            {
                this.start = start;
                this.koniec = koniec;
                this.waga = waga;
            }

            public override string ToString()
            {
                return $"{this.start} - {this.koniec} ({this.waga})";
            }

            public Node ZnajdzDrugi(Node n)
            {
                return n == this.start ? this.koniec : this.start;
            }
        }
        class Graf
        {
            public List<Node> nodes;
            public List<Krawedz> krawedzie;
            public List<Node> odwiedzony;
            public Graf()
            {
                this.nodes = new List<Node>();
                this.krawedzie = new List<Krawedz>();
                this.odwiedzony = new List<Node>();
            }
            public List<Krawedz> ZnajdzKrawedzie(Node n)
            {
                List<Krawedz> wynik = new List<Krawedz>();
                for (int i = 0; i < this.krawedzie.Count; i++)
                {
                    var k = this.krawedzie[i];
                    if(k.start == n || k.koniec == n )
                    {
                        wynik.Add(k);
                    }
                }
                return wynik;
                return this.krawedzie.Where(k => k.start == n || k.koniec == n).ToList();
            }
            public bool CzyNalezy(Node n)
            {
                for(int i = 0; i < odwiedzony.Count; i++)
                {
                    if(odwiedzony[i] == n)
                    {
                        return true;
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }
    }
}
