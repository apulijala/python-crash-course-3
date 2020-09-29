from messages import * 
import unittest


class Messages(unittest.TestCase):
    @unittest.skip
    def test_show_messages(self):
        mantras = ["Jaya Guru Datta", "Om Aim Hreem Shreem Kleem Sree Mathre Namaha"]
        show_messages(mantras)
        

    @unittest.skip
    
    def test_show_messages_copy(self):
        gurumantras = ["Jaya Guru Datta", "Om Aim Hreem Shreem Kleem Sree Mathre Namaha"]
        recitedmantras = []
        recitedmantras =  copy_after_show(gurumantras, recitedmantras)
        print(recitedmantras)
        gurumantras = ["Jaya Guru Datta", "Om Aim Hreem Shreem Kleem Sree Mathre Namaha"]
        self.assertEqual(gurumantras, recitedmantras)

    """
    8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function 
    send_messages() with a copy of the list of messages. After calling the function, 
    print both of your lists to show that the original list has retained its messages.
    """

   
    def test_show_messages_copy_again(self):
        gurumantras = ["Jaya Guru Datta", "Om Aim Hreem Shreem Kleem Sree Mathre Namaha"]
        recitedmantras = []
        copy_after_show(gurumantras[:], recitedmantras)
        print(recitedmantras)
        self.assertEqual(gurumantras, recitedmantras)





if __name__ == "__main__":
    unittest.main()
