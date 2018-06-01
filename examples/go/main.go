package main

import (
	"fmt"
	"golang.org/x/net/context"
	grpc "google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
	if err != nil {
		fmt.Printf("%+v\n", err)
	}
	defer conn.Close()

	client := NewSentimentClient(conn)
	for i := 0; i < 1000; i++ {
		client.Analyze(context.Background(), &SentimentRequest{Text: "The display resolution is fantastic and the speakers are crisp and clear."})
	}
	feature, err := client.Analyze(context.Background(), &SentimentRequest{Text: "hello"})
	if err != nil {
		fmt.Printf("%+v\n", err)
	}

	fmt.Printf("%+v\n", feature)
}
