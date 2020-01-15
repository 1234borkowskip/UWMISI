using System;

namespace ghgfgg
{
    class Program
    {
        static void Main(string[] args)
        {
            Pizza mala = new Mała();
            mala = new Pieczarki(mala);
            mala = new Szynka(mala);
            Console.WriteLine(mala.Opis() + " kosztuje " + $"{mala.Koszt()}");
            Pizza srednia = new Średnia();
            srednia = new Szynka(srednia);
            srednia = new Serx2(srednia);
            Console.WriteLine(srednia.Opis() + " kosztuje " + $"{srednia.Koszt()}");
            Pizza duza = new Duża();
            duza = new Kurczak(duza);
            duza = new Ananas(duza);
            Console.WriteLine(duza.Opis() + " kosztuje " + $"{duza.Koszt()}");
            Console.ReadKey();
        }

        public abstract class Pizza
        {
            public abstract double Koszt();
            public abstract string Opis();
        }

        public class Mała : Pizza
        {
            public override double Koszt()
            {
                return 15.00;
            }

            public override string Opis()
            {
                return "Mała pizza";
            }
        }



        public class Średnia : Pizza
        {
            public override double Koszt()
            {
                return 20.00;
            }

            public override string Opis()
            {
                return "Średnia pizza";
            }
        }

        public class Duża : Pizza
        {
            public override double Koszt()
            {
                return 25.00;
            }

            public override string Opis()
            {
                return "Duża pizza";
            }
        }

        public abstract class PizzaDekorator : Pizza
        {
            protected Pizza pizza;
            public PizzaDekorator(Pizza _pizza)
            {
                pizza = _pizza;
            }

            public override string Opis()
            {
                return pizza.Opis();
            }

            public override double Koszt()
            {
                return pizza.Koszt();
            }
        }

        class Pieczarki : PizzaDekorator
        {
            public Pieczarki(Pizza _pizza) : base(_pizza)
            {
            }

            public override double Koszt()
            {
                return 1.20 + pizza.Koszt();
            }

            public override string Opis()
            {
                return pizza.Opis() + ", pieczarki";
            }
        }

        class Szynka : PizzaDekorator
        {
            public Szynka(Pizza _pizza) : base(_pizza)
            {
            }

            public override double Koszt()
            {
                return 1.50 + pizza.Koszt();
            }

            public override string Opis()
            {
                return pizza.Opis() + ", szynka";
            }
        }

        class Serx2 : PizzaDekorator
        {
            public Serx2(Pizza _pizza) : base(_pizza)
            {
            }

            public override double Koszt()
            {
                return 1.50 + pizza.Koszt();
            }

            public override string Opis()
            {
                return pizza.Opis() + ", z podwójnym serem";
            }
        }

        class Kurczak : PizzaDekorator
        {
            public Kurczak(Pizza _pizza) : base(_pizza)
            {
            }

            public override double Koszt()
            {
                return 2 + pizza.Koszt();
            }

            public override string Opis()
            {
                return pizza.Opis() + ", kurczak";
            }
        }

        class Ananas : PizzaDekorator
        {
            public Ananas(Pizza _pizza) : base(_pizza)
            {
            }

            public override double Koszt()
            {
                return 1.2 + pizza.Koszt();
            }

            public override string Opis()
            {
                return pizza.Opis() + ", jakimś cudem z ananasem co moim zdaniem powinno zostać zakazane przez Konwencje o broni biologicznej w 1972 roku";
            }
        }

    }
}
