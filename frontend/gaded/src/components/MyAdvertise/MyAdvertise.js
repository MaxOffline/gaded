import React,{ Component} from 'react';
import * as asyncActions from '../Reducers/AdvertiseReducer/AsyncAdvertiseActions';
import { connect } from 'react-redux';
import AdvertiseCard from '../AdvertiseCart/AdvertiseCart';
import {Col,Row,Container, Button} from 'reactstrap';
import * as classes from './MyAdvertise.module.css'
import DeleteConfirme from '../DeleteConfirm/DeleteConfirme';
import { Pagination, PaginationItem, PaginationLink } from 'reactstrap';



class MyAdvertises extends Component{





    componentDidMount(){
        this.props.getMyAdveriseList(this.props.token)
    }
        

    AdertiseDetails=(item)=>{

        this.props.history.push('/advertise-detail/',item)
      }

      editHandler = (item) =>{
          item.from='edit'
          this.props.history.push('/edit-advertise/',item)
      }
      paginateNext=()=>{
            this.props.paginate('myAdvertise',this.props.myAdvertises.next,this.props.token)
      }
      paginateprevious=()=>{
        this.props.paginate('myAdvertise',this.props.myAdvertises.previous.this.props.token)
  }
    // deleteHandler=(item)=>{
    //     this.setState({modalOpend:!this.state.modalOpend,selectedItem:item})
    // }

    render(){

        let mapedAdvertises =null;
        if ( this.props.myAdvertises ){
            mapedAdvertises=(
                <Container>
                  <Row  >    
                    {this.props.myAdvertises.results.map(item=>
                        <Col lg='4' sm='12' md='6' key={item.id}>
                            <AdvertiseCard
                            title={item.title}
                            details={<div className={classes.btnContainer}>
                            <Button 
                            onClick={()=>this.AdertiseDetails(item)}
                            outline color="success">Details</Button>
                            <Button outline color="warning"
                            onClick={()=>this.editHandler(item)}
                            >Edite</Button>
                            <DeleteConfirme 
                                item={item}
                                buttonLabel={'Delete'}
                                />

                            </div>}
                            since={item.since}
                            img={item.image_1}   
                            price={item.price}
                            
                            />    
                           
                        </Col>

                    )}
                </Row>
                
        
                </Container>
            )
        }
    
    

        if ( !localStorage.getItem('token')){
            return (
                <h1 className={classes.paragraph}>please log in </h1>
            )
        }else if ( this.props.myAdvertises.results.length ===0){

    
            return (
    
                <>
                <h1 className={classes.paragraph}>Sorry you have no advertises Yet</h1>
                </>
            )
    
        }else{
            return (
    
                <>
                {mapedAdvertises}
                <div className={classes.paginatorContainer} >
                <Pagination size="lg"  aria-label="Page navigation example">

                        <PaginationItem disabled={!this.props.myAdvertises.previous}>
                            <PaginationLink previous  onClick={this.paginateprevious}/>
                        </PaginationItem>

                        <PaginationItem disabled={!this.props.myAdvertises.next}>
                            <PaginationLink next   onClick={this.paginateNext}/>
                        </PaginationItem>
                 </Pagination>
                 </div>

                </>
            )
        }
        
    }
    }



    

   
    


const mapActionToProps = dispatch =>{

    return {
        getMyAdveriseList:(token)=>dispatch(asyncActions.asyncMyAdvertiseList(token)),
        paginate:(source,link,token)=>dispatch(asyncActions.Paginate(source,link,token))
    }
}


const mapStateToProps = state =>{
    return {
        myAdvertises:state.advertise.myAdvertiseList,
        token:state.auth.token
    }
}

export default connect(mapStateToProps,mapActionToProps)(MyAdvertises) ;