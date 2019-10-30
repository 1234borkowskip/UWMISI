using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cw4
{
    class Osoba
    {
        public string imie;
        public string nazwisko;
        public int dataUrodzenia;

        public Osoba(string imie, string nazwisko, int dataUrodzenia)
        {
            this.imie = imie;
            this.nazwisko = nazwisko;
            this.dataUrodzenia = dataUrodzenia;
        }

        public void Wypiszinfo()
        {
            Console.WriteLine(imie + " " + nazwisko + " " + dataUrodzenia);
        }
    }
}
