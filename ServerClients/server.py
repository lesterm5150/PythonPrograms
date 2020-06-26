import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            self.request.send("Connection Succesful, what is your name?".encode())
            self.name = self.request.recv(1024)
            self.name = self.name.decode()
            #self.data = self.request.recv(1024)
            #self.data = self.data.decode()
            msg = str( "Welcome, " + self.name)
            
            if not self.name:
                print('DISCONNECTED')
                break
            self.request.send(msg.encode())
            print(self.name ,"connected.")
            questions = []
            answers = []
            while(True) :
                self.request.sendall("1. Play trivia game".encode())
                self.request.sendall("2. Submit a question\n".encode())
                choice = self.request.recv(1024)
                choice = int(choice.decode())
                if(choice == 1) :
                    question_num = 1
                    self.request.sendall("All right, let's play Friend Trivia\n".encode())
                    q = open('questions.txt', 'r')
                    a = open('answers.txt', 'r')
                    for line in q :
                        questions.append(line)
                    for line in a :
                        answers.append(line)
                    q.close()
                    a.close()
                    self.score = 0
                    
                    for q in questions :
                        q_msg = "Question #" + str(question_num) +"\n"
                        self.request.sendall(q_msg.encode())
                        self.request.sendall(q.encode())
                        
                        self.answer = self.request.recv(1024)
                        self.answer= str(self.answer.decode())
                        print(self.answer)
                        if ( self.answer.strip() == str(answers[question_num - 1]).strip()) :
                            self.request.send("That is correct!".encode())
                        else :
                            send_msg = "That is incorrect, the correct answer is : " + answers[question_num -1]
                            self.request.send(send_msg.encode())
                        question_num += 1
                        

                elif(choice == 2) :
                    self.request.send("First send your question then send the answer".encode())
                    
                

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
