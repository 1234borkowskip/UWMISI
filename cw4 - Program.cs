using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cw4
{
    class Program
    {
        static void Main(string[] args)
        {
            Osoba ja = new Osoba("x", "DDDDDD", 1999);
            ja.Wypiszinfo();
            Student ja2 = new Student("x", "DDDD", 1999, 2, 1, 151280);
            ja2.Wypiszinfo();
            Console.ReadKey();

        }
    }
}
