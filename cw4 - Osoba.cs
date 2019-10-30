using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cw4
{
    class Osoba
    {
        protected string imie;
        protected string nazwisko;
        protected int dataUrodzenia;

        protected Osoba(string imie, string nazwisko, int dataUrodzenia)
        {
            this.imie = imie;
            this.nazwisko = nazwisko;
            this.dataUrodzenia = dataUrodzenia;
        }

        protected void Wypiszinfo()
        {
            Console.WriteLine(imie + " " + nazwisko + " " + dataUrodzenia);
        }
    }
}
