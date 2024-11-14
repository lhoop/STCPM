module ASCON_TOP(
    input clk,
    input [319:0] Plaintext,
    output reg [319:0] Ciphertext
);

    reg [319:0] reg_in, reg_out;

    // Define the ASCON component
    LinearLayer ASCON_instance (
        .input_A(reg_in),
        .output_B(reg_out)
    );

    always @(posedge clk) begin
        reg_in <= Plaintext;
        Ciphertext <= reg_out;
    end

endmodule
module LinearLayer(
    input  clk,
    input rst,
    input [319:0] input_A,
    output [319:0] output_B


);
 
wire [63:0] A [0:4];
wire [63:0] B [0:4];
wire [63:0] ta [0:2];
wire [63:0] tb [0:4];
wire [63:0] tc [0:4];
wire [63:0] Sbox_out [0:4];
wire [63:0] c0 = 240;
assign {A[0], A[1], A[2], A[3], A[4]} = input_A;


assign ta[0] = A[0]^A[4] ;
assign ta[1]=  A[1]^A[2];
assign ta[2] = A[3]^A[4];

assign tb[0] = (~ta[0])&A[1] ;
assign tb[1]=  (~A[1])& ta[1] ;
assign tb[2] = (~ta[1])& A[3];
assign tb[3]=  (~A[3])&  ta[2];
assign tb[4] = (~ta[2])&  ta[0];

assign tc[0] = ta[0] ^ tb[1] ;
assign tc[1]=  A[1] ^ tb[2] ;
assign tc[2] =  ta[1] ^ tb[3];
assign tc[3]=  A[3] ^ tb[4];
assign tc[4] = ta[2] ^ tb[0];

assign Sbox_out[0] = tc[0] ^tc[4];
assign Sbox_out[1] =  tc[0] ^tc[1];
assign Sbox_out[2] =~tc[2] ;
assign Sbox_out[3] = tc[2] ^tc[3];
assign Sbox_out[4] = tc[4];




assign B[0] = Sbox_out[0] ^ {Sbox_out[0][18:0],Sbox_out[0][63:19]} ^ {Sbox_out[0][27:0],Sbox_out[0][63:28]};
assign B[1] = Sbox_out[1] ^ {Sbox_out[1][60:0],Sbox_out[1][63:61]} ^ {Sbox_out[1][38:0],Sbox_out[1][63:39]};
assign B[2] = Sbox_out[2] ^ {Sbox_out[2][0:0],Sbox_out[2][63:1]} ^ {Sbox_out[2][5:0],Sbox_out[2][63:6]}^c0;
assign B[3] = Sbox_out[3] ^ {Sbox_out[3][9:0],Sbox_out[3][63:10]} ^ {Sbox_out[3][16:0],Sbox_out[3][63:17]};
assign B[4] = Sbox_out[4] ^ {Sbox_out[4][6:0],Sbox_out[4][63:7]} ^ {Sbox_out[4][40:0],Sbox_out[4][63:41]};







assign output_B={B[0], B[1], B[2], B[3], B[4]};

endmodule