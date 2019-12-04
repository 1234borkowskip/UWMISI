using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp20
{
    class Program
    {
        static void Main(string[] args)
        {
        }
        class Graf
        {
            List<Node> odwiedzone;
        }
        public void PrzejscieDFS()
        {
            this.odwiedzone = new List<Node>();
            this.DFS(start);
            //wypisać liste odwiedzonych
        }
        public void DFS(Node n)
        {
            if (this.odwiedzone.Contains(n)) //sprawdzam czy odwiedzony
                return;
            this.odwiedzone.Add(n);
            var krawedzieOd = this.ZnajdzKrawedzie(n);   // wszystkie krawedzie z node n
            foreach(var k in krawedzieOd)
            {
                var drugi = k.WezDrugi(n); //drugi wierzcholek
                DFS(drugi); // powtórz
            }
        }


    }
}
